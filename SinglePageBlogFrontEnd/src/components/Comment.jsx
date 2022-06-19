import axios from "axios";
import React, { useState } from "react";

function Comment({ id }) {
  const [comments, setComments] = useState([]);
  const [commentBtnName, setCommentBtnName] = useState("show comments");
  function ShowComments() {
    return comments.map((comment) => (
      <div className="comment-div" key={comment.id}>
        <span>{comment.user.username}</span>
        <p>{comment.text}</p>
      </div>
    ));
  }
  const fetchComments = () => {
    axios
      .get(`https://singleblog.pythonanywhere.com/comments/${id}`)
      .then((res) => {
        if (res.status == 200) {
          console.log(res.data);
          setComments(res.data);
          setCommentBtnName("hide comments");
        }
      });
  };
  const hideComments = () => {
    setComments([]);
    setCommentBtnName("show comments");
  };
  return (
    <div>
      {commentBtnName === "hide comments" ? <ShowComments></ShowComments> : ""}
      <button
        onClick={
          commentBtnName === "show comments" ? fetchComments : hideComments
        }
        className="btn btn-secondary show-comments btn-sm my-2"
      >
        {commentBtnName}
      </button>
    </div>
  );
}

export default Comment;
