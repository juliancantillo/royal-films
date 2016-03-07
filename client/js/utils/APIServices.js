export default class APIService {

	// methods
	static fetchData (action = '', fn = null) {
    let url = `/api/v1/${action}`;

    fetch(url)
    .then((response) => {
        if (response.status !== 200) {
          console.log('Looks like there was a problem. Status Code: ' +
            response.status);
          return;
        }

        return response
      }
    )
    .then(fn)
    .catch((err) => {
      console.log('Fetch Error :-S', err);
    });
  }
}
