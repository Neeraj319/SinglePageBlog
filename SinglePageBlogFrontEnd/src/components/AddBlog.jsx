import React, { useState, useContext } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import UserContext from "./UserContext";
function AddBlog() {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const history = useHistory();
  const check_validation = useContext(UserContext);
  if (check_validation.token !== null) {
    const postBlog = () => {
      if (title === "" && body === "") {
        alert("fields cant be empty");
      } else {
        axios
          .post(
            "https://singleblog.pythonanywhere.com/",
            {
              title: title,
              body: body,
            },
            {
              headers: {
                Authorization: check_validation.token,
                "Content-Type": "application/json",
              },
            }
          )
          .then((res) => {
            console.log(res);
            if (res.status === 201) {
              alert("blog created successfully");
              history.push("/");
            } else {
              alert("something went wrong");
            }
          })
          .catch((err) => console.log(err));
      }
    };
    return (
      <div className="container">
        <div className="form-div">
          <input
            value={title}
            className="form-control"
            placeholder="title here"
            onChange={(e) => setTitle(e.target.value)}
          />
          <textarea
            value={body}
            className="form-control my-1"
            rows="5"
            onChange={(e) => {
              setBody(e.target.value);
            }}
          ></textarea>
          <div className="d-grid gap-2">
            <button
              className="btn btn-outline-success"
              type="button"
              onClick={postBlog}
            >
              Post Blog
            </button>
          </div>
        </div>
      </div>
    );
  } else {
    return (
      <h1>
        redirecting
        {history.push("/login")}
      </h1>
    );
  }
}

export default AddBlog;
