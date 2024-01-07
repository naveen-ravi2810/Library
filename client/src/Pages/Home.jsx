import React from 'react'
import { Link } from 'react-router-dom'
export const Home = () => {
  return (
    <div>
        <div>
            <Link to='/login'><button>Login</button></Link>
        </div>
    </div>
  )
}
