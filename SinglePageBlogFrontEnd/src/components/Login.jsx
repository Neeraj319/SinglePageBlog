import axios from "axios";
import React, { useContext, useState } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "./UserContext";
function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const history = useHistory();
  const check_validation = useContext(UserContext);
  if (check_validation.token === null) {
    const login = () => {
      if (username === "" && password === "") {
        alert("fields cant be empty");
      } else {
        axios
          .post(
            "https://singleblog.pythonanywhere.com/auth/login",
            {
              username: username,
              password: password,
            },
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          )
          .then((res) => {
            if (res.status === 200) {
              console.log("hello");
              localStorage.setItem("token", "Token " + res.data);
              window.location.reload();
            } else {
              alert("invalid password or username");
            }
          })
          .catch((err) => {
            alert("invalid password or username");
          });
      }
    };
    return (
      <div className="login-from">
        <div className="container">
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="form-control my-2"
            placeholder="username"
          ></input>
          <input
            className="form-control"
            value={password}
            type="password"
            placeholder="password"
            onChange={(e) => setPassword(e.target.value)}
          ></input>
          <div className="d-grid gap-2 col-6 mx-auto">
            <button
              className="btn btn-primary my-2"
              type="button"
              onClick={login}
            >
              Login
            </button>
          </div>
        </div>
      </div>
    );
  } else {
    return (
      <h1>
        redirecting
        {history.push("/")}
      </h1>
    );
  }
}

export default Login;
