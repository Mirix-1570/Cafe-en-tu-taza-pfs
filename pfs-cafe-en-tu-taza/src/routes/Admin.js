import React from 'react';
import { Routes, Route } from 'react-router-dom';
import AdminDashboard from '../components/AdminDashboard';
import ProductAdmin from '../components/Admin/ProductAdmin/ProductAdmin';
import ProductForm from '../components/ProductForm';

const Admin = () => {
    return (
        <Routes>
            <Route path="/" element={<AdminDashboard />} />
            <Route path="/products" element={<ProductAdmin />} />
            <Route path="/products/new" element={<ProductForm />} />
            <Route path="/products/edit/:id" element={<ProductForm />} />
        </Routes>
    );
};

export default Admin;
