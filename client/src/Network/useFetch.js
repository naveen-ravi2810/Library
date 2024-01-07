import React, { useEffect, useState } from 'react'

export const useGet = ({url, token}) => {
    const [data, setData] = useState(null);
    useEffect(() => {
        fetch(url,{
            headers : {
                'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEzLCJleHAiOjE3MDQ1MTkyMjguOTUwMDIwMywicm9sZSI6InJlYWRlciIsImlhdCI6MTcwNDUxODYyOC45NTAwMjMyfQ.MrAp9brkkye_xleIng656QdKZwCljmNnWzxucAbFIEs'
            }
        })
          .then((res) => res.json())
          .then((data) => setData(data));
      }, [url]);
    
      return [data];
}

export const useLogin = (data) => {
    const [data, setdata] = useState(null);
    useEffect(()=>{
        fetch('http://127.0.0.1:8000/api/v1/user/login',{
            headers:{
                'Content-Type' : 'application/json'
            },
            body:data
        })
        .then((res)=>res.json())
        .then((data)=>setdata(data))
    }, [url])
    return [data]
}
