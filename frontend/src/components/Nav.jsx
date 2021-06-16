import React, { useContext } from "react";
import { Link } from "react-router-dom";
import Login from "./Login";
import UserContext from "./UserContext";

export default function Nav() {
  const username = useContext(UserContext);
  return (
    <div>
      <div className="container">
        <header className="d-flex justify-content-center py-3">
          <ul className="nav nav-pills">
            <li className="nav-item">
              <Link to="/" className="nav-link active">
                Home
              </Link>
            </li>
            <li className="nav-item">
              {username.username !== "" ? (
                <Link to="/addblog" className="nav-link">
                  Add Blog
                </Link>
              ) : (
                <Link to="/login" className="nav-link">
                  Login
                </Link>
              )}
            </li>
            <li className="nav-item">
              {username.username !== "" ? (
                <Link to={"/profile/" + username.username} className="nav-link">
                  My profile
                </Link>
              ) : (
                <Link to={"/signup"} className="nav-link">
                  sign up
                </Link>
              )}
            </li>
          </ul>
        </header>
      </div>
    </div>
  );
}
