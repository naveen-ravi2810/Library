import { BrowserRouter, Routes, Route } from "react-router-dom"
import { Router } from "./Router"
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/*" element={<Router/>}/>
      </Routes>
    </BrowserRouter>
  )
}