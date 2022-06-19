import axios from "axios";
import React, { Component, useEffect, useState } from "react";
import AddLike from "./AddLike";
import Comment from "./Comment";
import { useHistory } from "react-router-dom";
import AddComment from "./AddComment";
function DetailBlog({ match }) {
  const [blog, setBlog] = useState({ title: "", body: "", likes: 0 });
  const id = match.url.split("/")[2];
  const history = useHistory();
  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/blog/${id}`)
      .then((res) => {
        if (res.status == 200) {
          const data = res.data;
          setBlog({
            title: data.title,
            body: data.body,
            likes: data.likes.length,
            user: data.user.username,
          });
        }
      })
      .catch((err) => {
        history.push("/");
      });
  }, [id]);
  return (
    <div className="container card">
      <h2>{blog.title}</h2>
      <span>written by:{blog.user}</span>
      <p>{blog.body}</p>
      <AddLike id={id}></AddLike>
      <Comment id={id}></Comment>
      <AddComment id={id}></AddComment>
    </div>
  );
}

export default DetailBlog;
