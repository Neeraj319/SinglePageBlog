import React from "react";
import AddLike from "./AddLike";
import { Link } from "react-router-dom";
import Comment from "./Comment";
import AddComment from "./AddComment";
function RenderBlogs({ Blog }) {
  return (
    <div>
      {Blog.map((data) => {
        return (
          <div className="container card mx-2 blog-card" key={data.id}>
            <Link to={`blog/${data.id}`} className="text-dark">
              <h3 className="text-dark">{data.title}</h3>
            </Link>
            <span>written by:{data.user.username}</span>

            <p>{data.body}</p>

            <AddLike id={data.id}></AddLike>
            <Comment id={data.id}></Comment>
            <AddComment id={data.id}></AddComment>
          </div>
        );
      })}
    </div>
  );
}

export default RenderBlogs;
