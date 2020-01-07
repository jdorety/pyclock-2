import React from "react"
import Layout from "../components/layout/layout"
import Header from "../components/header/header"

export default () => (
  <div style={{ color: `teal` }}>
    <Layout>
      <Header headerText="About Gatsby" />
      <p>Such wow. Very React.</p>
    </Layout>
  </div>
)
