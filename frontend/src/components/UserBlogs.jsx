import React, { useEffect, useState, useContext } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { useHistory } from "react-router-dom";
import UserContext from "./UserContext";
export default function UserBlogs({ username }) {
  const [Blog, setBlog] = useState([]);
  const history = useHistory();
  const check_validation = useContext(UserContext);
  if (check_validation.token === null) {
    return (
      <div>
        redirecting
        {history.push("/")}
      </div>
    );
  }
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/auth/userblogs", {
        headers: {
          Authorization: check_validation.token,
        },
      })
      .then((res) => {
        if (res.status == 200) {
          setBlog(res.data);
        } else {
          console.log("something went wrong");
        }
      })
      .catch((err) => console.log(err));
  }, []);
  return (
    <div className="card-text">
      {Blog.length === 0
        ? "No Blogs"
        : Blog.map((data) => (
            <div className="card-text">
              <Link to={`/blog/${data.id}`} className="text-dark">
                <h5 className="text-dark">{data.title}</h5>
              </Link>
            </div>
          ))}
    </div>
  );
}
