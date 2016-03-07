import React from 'react';
import CinemasList from './CinemasList'
import APIServices from '../utils/APIServices'

export default class MovieShowtime extends React.Component {
  static propTypes = {
    movie: React.PropTypes.string,
  };

  constructor(props) {
    super(props);

    this.state = {
      functions: [],
      filtered: []
    };
  }

  componentDidMount() {
    let movie = this.props.movie;

    APIServices.fetchData(`showtimes/${movie}`,(response) => {
      // Examine the text in the response
      response.json().then((data) => {

        this.setState({
          functions: data.results,
          filtered: data.results
        });
      });
    });
  }

  cinemaChangeHandler(e){
    console.log('Cinema changed', e.target.value);

    let uuid = e.target.value,
        filtered_functs = this.state.functions

    if (uuid) {
      filtered_functs = filtered_functs.filter((value) => {
        return value.cinema.uuid === uuid;
      });
    }

    this.setState({
      filtered: filtered_functs
    });

  }

  render() {


    let cinemaList = this.state.functions.map((funct) => {
      return (<option key={funct.cinema.uuid} value={funct.cinema.uuid}>{funct.cinema.name}</option>)
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
      <CinemasList cinemas={this.state.filtered} />
    </div>
    );
  }
}
