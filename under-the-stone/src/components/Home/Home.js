import { useState } from "react";


export const Home = () => {
    console.log("wat");
    const [counter, setCounter] = useState(0);
     
    return (
        <div style={{
            backgroundImage: `url(${process.env.PUBLIC_URL + 'main-page.jpg'})`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            width: '100vw',
            height: '100vh',
            opacity: '86%'
             

         }}>
            <div>APP THIS UP</div>
        
        </div>


        );

};

