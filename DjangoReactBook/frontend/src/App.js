/* backend/ rest / api imports */

/* react imports */
import {useState, useEffect } from 'react'

/* styling imports */
import logo from './logo.svg';
import './App.css';
import './index.js'

/* pages */


/* usestate
the usestate/initial state is books with an empty array
useEffect is inserting books into the usestate
printing them with .map
*/


function App() {
    const [books, setBooks] = useState([])
/* fetch the books */
useEffect (() => {
    async function fetchBooks() {
        const res = await fetch("http://127.0.0.1:8000/bookslist/");
        res.json()
        .then(res => setBooks(res.response))
        .catch(err => setErrors(err));
    }
    fetchBooks();
},[])
/* display the books */ 
    useEffect (() => {
            setBooks([
                {
                "name":"Otostopçunun Galaksi Rehberi", 
                "author":    "Douglas Adams", 
                "description": "Lorem ipsum"
                },
                {
                "name":"Hikayeler", 
                "author":    "Edgar Allan Poe", 
                "description": "Lorem ipsum sit door amet"
                }
            ])
    },[])
/* =================== */
/* RETURN */
/* =================== */
        return (
            books.map((book,index) => {
                return (
                    <div className="book-item">
                        <h2>{book.name}</h2>
                        <p>{book.author}</p>
                        <p>{book.description}</p>
                    </div>
                )}
                )
        );
    }
export default App;
