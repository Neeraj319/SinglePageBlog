import axios from "axios";
import React, { useContext, useEffect, useState } from "react";
import UserBlogs from "./UserBlogs";
import UserContext from "./UserContext";
function RenderUserDetails({ userProfileDetails }) {
  return (
    <h5 className="card-title">
      <h3> Blogs of {userProfileDetails.username}</h3>
    </h5>
  );
}
function UserProfile({ match }) {
  const token = useContext(UserContext);
  const [userProfile, setUserProfile] = useState({
    username: "",
  });
  useEffect(() => {
    axios
      .get(
        "https://singleblog.pythonanywhere.com/auth/user/" +
          match.url.split("/")[2],
        {
          headers: {
            Authorization: token.token,
          },
        }
      )
      .then((res) => {
        setUserProfile({
          username: res.data.username,
        });
      });
  }, []);
  return (
    <div className="container">
      <div className="card">
        <div className="card-body">
          <RenderUserDetails
            userProfileDetails={userProfile}
          ></RenderUserDetails>
          <UserBlogs username={match.url.split("/")[2]}></UserBlogs>
        </div>
      </div>
    </div>
  );
}

export default UserProfile;
