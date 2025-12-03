import React, { useState, useEffect } from 'react';
import { fetchAllProducts } from '../../../services/products';

function ProductAdmin() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetchAllProducts()
      .then(data => setProductos(data))
      .catch(error => console.error(error));
  }, []); // El array vacío asegura que se ejecute solo una vez al montar el componente

  return (
    <div>
      {productos.map(producto => (
        <div key={producto.id} className="p-4 border rounded shadow-md mb-4">
          <div className="flex items-center justify-between mb-2">
            <input
              type="text"
              className="text-lg font-semibold"
              value={producto.nombre}
              readOnly // Para que no sea editable directamente en esta vista
            />
            <label className="switch">
              <input type="checkbox" checked={producto.estatus} readOnly />
              <span className="slider round"></span>
            </label>
          </div>
          <p className="text-gray-600">Estatus: {producto.estatus ? 'Activo' : 'Inactivo'}</p>
        </div>
      ))}
    </div>
  )
}

export default ProductAdmin