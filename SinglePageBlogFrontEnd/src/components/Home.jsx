import React, { useEffect, useState } from "react";
import axios from "axios";
import RenderBlogs from "./RenderBlogs";

export default function Home() {
  const [Blog, setBlog] = useState([]);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/")
      .then((res) => {
        if (res.status == 200) {
          setBlog(res.data);
        } else {
          console.log("some error occurred");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <div className="home-blog-div">
      <div className="container">
        <RenderBlogs Blog={Blog}></RenderBlogs>
      </div>
    </div>
  );
}
