import '../App.css';
import '../api.js'



function Offers() {

    const fetchResponse = async () => {
        const response = await api.get('/index');
        console.log(response);
    }



    return (
      <div className="Offers">
        <header className="App-header">
          <p>
          Offers example page!!!
          </p>


          <h2> {fetchResponse()} </h2>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Offers example page!!!
          </a>
        </header>
      </div>
    );
  }
  
  export default Offers;