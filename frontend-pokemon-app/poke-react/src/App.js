/* eslint-disable */
import React from 'react';
import {Component} from 'react';
import "./App.css"
import Header from './components/Header'
import PokeCard from './components/PokeCard'

class App extends Component {
  constructor() {
    super();
    this.state = {
      pokemons : [],
      pokemonDetails : [],

    }
    this.handleMoreClick = this.handleMoreClick.bind(this);
  }

  

  handleMoreClick(event) {
      console.log("Offset: " + this.state.pokemon)
    };
    
  
  
  componentDidMount() {
    this.getMorePokemon();
  }

  getMorePokemon() {
    let url = "https://backend-pokemon-app.herokuapp.com/api/v1/all_pokemons"
    console.log(url);
    fetch(url)
    .then(response => response.json())
    .then(data => {
      if (data) {
        this.setState({pokemonDetails: data.results})
      }
    })
    .catch(console.log)
  }

  render() {
    const {pokemonDetails} = this.state;
    const renderedPokemonList = pokemonDetails.map((pokemon,index) => {
      return (<PokeCard key={index} pokemon={pokemon} />);
    });

    return (
      <div>
        <Header />
        <div className="container">
          <div className="card-columns">
         
            {renderedPokemonList}
          </div>
        </div>
      
      </div>
    );
  }
}

export default App;
