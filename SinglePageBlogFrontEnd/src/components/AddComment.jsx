import axios from "axios";
import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "./UserContext";
export default function AddComment({ id }) {
  const [comment, setComment] = useState("");
  const [rows, setRows] = useState(1);
  const history = useHistory();
  const check_validation = useContext(UserContext);
  const postComment = () => {
    if (check_validation.token === null) {
      history.push("/login");
    } else {
      if (comment === "") {
      } else {
        axios
          .post(
            `https://singleblog.pythonanywhere.com/add_comment/${id}`,
            {
              text: comment,
            },
            {
              headers: {
                Authorization: check_validation.token,
                "Content-Type": "application/json",
              },
            }
          )
          .then((res) => {
            if (res.status === 201) {
              alert("comment added successfully");
            } else {
              alert("server error");
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    }
  };
  return (
    <div className="add-comment">
      <textarea
        rows={rows}
        className="form-control my-2"
        value={comment}
        onChange={(e) => {
          setComment(e.target.value);
          e.target.style.height = e.target.scrollHeight + "px";
        }}
      ></textarea>
      <button className="btn btn-success my-2" onClick={postComment}>
        add comment
      </button>
    </div>
  );
}
