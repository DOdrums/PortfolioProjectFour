// code taken from DOdrums github 'UCDresume' project, written as walkthrough
// of a Code Institute project. Display google map in footer.
function initMap() {
    const myLatLng = { lat: 52.05987500216573, lng: 4.25453638650689 };
    var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15,
      center: {
        lat: 52.05987500216573,
        lng: 4.25453638650689
      }
    });

    var label = "NailsbyFaar";

    var locations = [{
        lat: 52.05987500216573,
        lng: 4.25453638650689
      },
    ];

    var markers = locations.map(function (location, i) {
      return new google.maps.Marker({
        position: location,
        label: label
      });
    });

    var markerCluster = new MarkerClusterer(map, markers, {
      imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });
  }