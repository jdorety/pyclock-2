import React from "react"
import { Link } from "gatsby"

import "./blogLink.scss"

export default props => {
  return (
    <Link to={props.path}>
      <div className="blog-link">
        <h3>{props.title}</h3>
      </div>
    </Link>
  )
}
