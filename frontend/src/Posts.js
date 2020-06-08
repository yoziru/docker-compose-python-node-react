import React from "react";
import useSWR from "swr";

export default function Posts() {
  const { data, error } = useSWR("/api/posts", (url) =>
    fetch(url).then((result) => result.json())
  );

  if (error) return <div>failed to load</div>;
  if (!data) return <div>loading...</div>;
  return (
    <div>
      {data.posts.map((post) => (
        <p key={post.id}>{post.content}</p>
      ))}
    </div>
  );
}
