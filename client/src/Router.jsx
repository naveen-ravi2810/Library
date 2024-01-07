import { Routes, Route } from "react-router-dom";

import React from 'react'
import { Dashboard, Home, Login } from "./Pages";

export const Router = () => {
  return (
    <Routes>
        <Route path="/">
        <Route path="/" Component={Home}/>
        <Route path="/login" Component={Login}/>
        <Route path="/dashboard" Component={Dashboard}/>
        </Route>
    </Routes>
  )
}
