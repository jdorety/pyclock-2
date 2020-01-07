import React from "react"
import NavBar from "./navbar/navbar"

export default ({ children }) => (
  <div style={{ margin: "3rem auto", maxWidth: 650, padding: "0 1rem" }}>
    <NavBar />
    {children}
  </div>
)
