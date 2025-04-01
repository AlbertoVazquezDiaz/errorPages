import React, { useEffect, useState } from "react";
import axios from "axios";
import DataTable from "react-data-table-component";
import Swal from "sweetalert2";

const UserDataTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  const accessToken = localStorage.getItem("accessToken");
  const refreshToken = localStorage.getItem("refreshToken");
  const currentUserId = localStorage.getItem("userId");

  const refreshAccessToken = async () => {
    if (!refreshToken) {
      Swal.fire("Sesión expirada", "Debes iniciar sesión nuevamente.", "warning").then(() => {
        localStorage.clear();
        window.location.href = "/login";
      });
      throw new Error("No hay refresh token");
    }

    try {
      const res = await axios.post("http://127.0.0.1:8000/users/token/refresh/", {
        refresh: refreshToken,
      });
      const newToken = res.data.access;
      localStorage.setItem("accessToken", newToken);
      return newToken;
    } catch (err) {
      Swal.fire("Sesión expirada", "Debes iniciar sesión nuevamente.", "warning").then(() => {
        localStorage.clear();
        window.location.href = "/login";
      });
      throw new Error("Refresh token inválido");
    }
  };

  const fetchUsers = async () => {
    setLoading(true);

    if (!accessToken) {
      await refreshAccessToken();
    }

    try {
      const res = await axios.get("http://127.0.0.1:8000/users/api/", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        },
      });
      setData(res.data);
    } catch (err) {
      if (err.response?.status === 401) {
        try {
          const newToken = await refreshAccessToken();
          const retryRes = await axios.get("http://127.0.0.1:8000/users/api/", {
            headers: {
              Authorization: `Bearer ${newToken}`,
            },
          });
          setData(retryRes.data);
        } catch (refreshError) {
          return; // ya redirigido
        }
      } else {
        Swal.fire("Error", "No se pudieron cargar los usuarios", "error");
      }
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleDelete = (user) => {
    const loggedUserId = parseInt(localStorage.getItem("userId"));
  
    if (!loggedUserId || user.id === loggedUserId) {
      Swal.fire("No permitido", "No puedes eliminarte a ti mismo", "warning");
      return;
    }
  
    Swal.fire({
      title: `¿Eliminar a ${user.name}?`,
      text: "Esta acción no se puede deshacer",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Sí, eliminar",
    }).then(async (result) => {
      if (result.isConfirmed) {
        try {
          await axios.delete(`http://127.0.0.1:8000/users/api/${user.id}/`, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
          });
          Swal.fire("¡Eliminado!", "El usuario fue eliminado exitosamente", "success");
          fetchUsers();
        } catch (err) {
          if (err.response?.status === 401) {
            try {
              const newToken = await refreshAccessToken();
              if (newToken) handleDelete(user);
            } catch {}
          } else {
            Swal.fire("Error", "No se pudo eliminar el usuario", "error");
          }
        }
      }
    });
  };
  

  const handleEdit = async (user) => {
    const { value: formValues } = await Swal.fire({
      title: `Editar a ${user.name}`,
      html:
        `<input id="swal-input1" class="swal2-input" value="${user.name}" placeholder="Nombre">` +
        `<input id="swal-input2" class="swal2-input" value="${user.email}" placeholder="Correo">` +
        `<input id="swal-input3" class="swal2-input" value="${user.tel || ""}" placeholder="Teléfono">`,
      focusConfirm: false,
      showCancelButton: true,
      confirmButtonText: "Guardar cambios",
      preConfirm: () => {
        const name = document.getElementById("swal-input1").value.trim();
        const email = document.getElementById("swal-input2").value.trim();
        const tel = document.getElementById("swal-input3").value.trim();

        if (!name || !email.includes("@")) {
          Swal.showValidationMessage("Nombre y correo válidos son requeridos.");
          return false;
        }

        return { name, email, tel };
      },
    });

    if (formValues) {
      const confirm = await Swal.fire({
        title: "¿Confirmar actualización?",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Sí, actualizar",
      });

      if (confirm.isConfirmed) {
        try {
          await axios.patch(
            `http://127.0.0.1:8000/users/api/${user.id}/`,
            formValues,
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
              },
            }
          );
          Swal.fire("Actualizado", "Usuario modificado correctamente", "success");
          fetchUsers();
        } catch (err) {
          if (err.response?.status === 401) {
            try {
              const newToken = await refreshAccessToken();
              if (newToken) handleEdit(user);
            } catch {}
          } else {
            Swal.fire("Error", "No se pudo actualizar el usuario", "error");
          }
        }
      }
    }
  };

  const columns = [
    { name: "Nombre", selector: (row) => row.name, sortable: true },
    { name: "Correo", selector: (row) => row.email, sortable: true },
    { name: "Teléfono", selector: (row) => row.tel || "No registrado" },
    {
      name: "Acciones",
      cell: (row) => (
        <>
          <button className="btn btn-warning me-2" onClick={() => handleEdit(row)}>
            <i className="bi bi-pencil"></i>
          </button>
          <button className="btn btn-danger" onClick={() => handleDelete(row)}>
            <i className="bi bi-trash"></i>
          </button>
        </>
      ),
    },
  ];

  return (
    <div className="container mt-4">
      <h3 className="mb-3">Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
    </div>
  );
};

export default UserDataTable;
