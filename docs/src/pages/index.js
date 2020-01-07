import React from "react"
import { graphql } from "gatsby"
import BlogLink from "../components/blogLink"

import Layout from "../components/layout/layout"

export default ({ data }) => (
  <Layout>
    <h1>Welocome to the PyClock2 Development Blog</h1>
    <p></p>
    {data.allMarkdownRemark.edges.map(post => {
      return (
        <BlogLink
          path={post.node.frontmatter.path}
          key={post.node.id}
          title={post.node.frontmatter.title}
          author={post.node.frontmatter.author}
        />
      )
    })}
  </Layout>
)
export const pageQuery = graphql`
query MyQuery {
  allMarkdownRemark(sort: {fields: frontmatter___date, order: ASC}) {
    edges {
      node {
        id
        html
        frontmatter {
          author
          date
          path
          title
        }
      }
    }
  }
}

`
