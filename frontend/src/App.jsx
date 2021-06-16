import React, { useContext, useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Nav from "./components/Nav";
import { Switch, Route } from "react-router-dom";
import Home from "./components/Home";
import AddBlog from "./components/AddBlog";
import UserProfile from "./components/USerProfile";
import axios from "axios";
import UserContext from "./components/UserContext";
import DetailBlog from "./components/DetailBlog";
import Login from "./components/Login";
import SignUp from "./components/SignUp";
function App() {
  const [username, setUsername] = useState("");

  const token = localStorage.getItem("token");
  if (token !== "") {
    useEffect(() => {
      axios
        .get("http://127.0.0.1:8000/auth/username", {
          headers: {
            Authorization: token,
          },
        })
        .then((res) => {
          setUsername(res.data.username);
        });
    }, [username]);
  } else {
    setUsername("");
  }
  return (
    <div className="App">
      <UserContext.Provider value={{ username: username, token: token }}>
        <Nav></Nav>
        <Switch>
          <Route path="/" exact component={Home}></Route>
          <Route path="/addblog" exact component={AddBlog}></Route>
          <Route
            path={"/profile/:" + username}
            exact
            component={UserProfile}
          ></Route>
          <Route path="/blog/:id" exact component={DetailBlog}></Route>
          <Route path="/login" exact component={Login}></Route>
          <Route path="/signup" exact component={SignUp}></Route>
          <Route render={() => <h1>Page not found 404</h1>}></Route>
        </Switch>
      </UserContext.Provider>
    </div>
  );
}

export default App;
