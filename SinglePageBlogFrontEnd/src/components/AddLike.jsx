import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import UserContext from "./UserContext";
function AddLike({ id }) {
  const [like, setLike] = useState(false);
  const [likeClass, setLikeClass] = useState("like");
  const [likes, setLikes] = useState(0);
  const history = useHistory();
  const check_validation = useContext(UserContext);
  const addLike = () => {
    if (check_validation.token === null) {
      console.log("hi");
      history.push("/login");
    } else {
      axios
        .post(
          `https://singleblog.pythonanywhere.com/like_blog/${id}`,
          {},
          {
            headers: {
              Authorization: check_validation.token,
              "Content-Type": "application/json",
            },
          }
        )
        .then((res) => {
          setLike(res.data.liked);
          setLikes(res.data.likes);
          res.data.liked ? setLikeClass("liked") : setLikeClass("like");
        })
        .catch((err) => console.log(err));
    }
  };
  useEffect(() => {
    axios
      .get(`https://singleblog.pythonanywhere.com/like_blog/${id}`)
      .then((res) => {
        if (res.data.liked) {
          setLike((like) => !like);
          setLikeClass("liked");
        }
        setLikes(res.data.likes);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <span>likes : {likes}</span>
      <button className={likeClass} onClick={addLike}>
        {like ? "liked" : "like"}
      </button>
    </div>
  );
}

export default AddLike;
