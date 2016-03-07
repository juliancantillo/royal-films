import React from 'react';
import MoviesList from './MoviesList'
import APIServices from '../utils/APIServices'

export default class ShowtimesForm extends React.Component {
  static propTypes = {
    movie: React.PropTypes.string,
  };

  constructor(props) {
    super(props);

    this.state = {
      cinemas: [],
      currentCinema: {},
      movies: [],
    };
  }



  componentDidMount() {

    APIServices.fetchData('cinemas/',(response) => {
      // Examine the text in the response
      response.json().then((data) => {

        this.setState({
          cinemas: data.results
        });
      });
    });
  }

  cinemaChangeHandler(e){
    console.log('Cinema changed', e.target.value);

    let uuid = e.target.value;
    let url = `cinemas/${uuid}/movies`;

    APIServices.fetchData(url, (response) => {
      // Examine the text in the response
      response.json().then((data) => {

        this.setState({
          movies: data.functions,
          currentCinema: data
        });
      });
    })
  }

  render() {


    let cinemaList = this.state.cinemas.map((cinema) => {
      return (<option key={cinema.uuid} value={cinema.uuid}>{cinema.name}</option>)
    });

    return (
    <div className="card">
      <div className="card-block">
        <h4 className="card-title">Showtimes</h4>
        <form action="" className="form">
          <div className="form-group row">
            <div className="col-sm-12">
              <select onChange={this.cinemaChangeHandler.bind(this)} className="form-control form-control-lg">
                <option value="" lable="Select cinema">Select cinema</option>
                {cinemaList}
              </select>
            </div>
          </div>
        </form>
      </div>
      <MoviesList movies={this.state.movies} />
    </div>
    );
  }
}
