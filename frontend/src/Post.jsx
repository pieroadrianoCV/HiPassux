import React from 'react';
import {HeaderPost} from './components/Header';
import apiFetch from './services/api-fetch';
//import { useEffect } from "react";

const Post = () => {
  useEffect(() => {
    apiFetch("posts")
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log(error)      });
  }, []);
  return (
    <div>
      <HeaderPost />
    </div>
  );
};

export default Post;
