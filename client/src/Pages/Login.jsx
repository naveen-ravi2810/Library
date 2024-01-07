import React, { useState } from 'react'
import { useLogin } from '../Network'

export const Login = () => {

    const [UserDetails, setUserDetails] = useState({})
    function UpdateLoginForm(event){
        setUserDetails({
            ...UserDetails,
            [event.target.name] : event.target.value
        })
    }

    function fn_Login(event){
        event.preventDefault()
        const books = useLogin(UserDetails)    
        console.log()
    }
    console.log(books)
    
  return (
    <div>
        <form onSubmit={fn_Login}>
            <div>
                <label>Username</label>
                <input type="text" name='user_name' onChange={UpdateLoginForm} required/>
            </div>
            <div>
                <label>Password</label>
                <input type="password" name='password' onChange={UpdateLoginForm} required/>
            </div>
            <div>
                <button type="submit">Login</button>
            </div>
        </form>
    </div>
  )
}
