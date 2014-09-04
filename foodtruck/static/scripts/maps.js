function initialize() {
  var mapOptions = {
    //center: new google.maps.LatLng(-34.397, 150.644),
    zoom: 16
  };
  var map = new google.maps.Map(document.getElementById("map-canvas"),mapOptions);
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                      position.coords.longitude);
      //var pos = new google.maps.LatLng(37.78116, -122.409178);
      
      var infoWnd = new google.maps.InfoWindow({
        map: map,
        position: pos,
        content: '<p style="color:red">Search Center</p>'
        
      });
      var lat = document.getElementById("id_latitude")
      lat.value = pos.lat()
      var lon = document.getElementById("id_longitude")
      lon.value = pos.lng()
      //$('#id_longitude').val(pos.lon())
      google.maps.event.addListener(map, "center_changed", function() {
        var cnt = map.getCenter();
        //infoWnd.setContent(cnt.toUrlValue());
        infoWnd.setPosition(cnt);
        lat = document.getElementById("id_latitude")
        lat.value = cnt.lat()
        lon = document.getElementById("id_longitude")
        lon.value = cnt.lng()
        infoWnd.open(map);
      });
      
      map.setCenter(pos);

      renderFoodTrucks(map);
    }, function() {
      handleNoGeolocation(true);
    });
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  } //endif

}

function renderFoodTrucks(map) {
  //console.log("renderFoodTrucks")
  var fts = document.getElementsByClassName("ft-info")
  for (var i = 0; i < fts.length; ++i) {
    console.log("renderFoodTrucks")
        var name = fts[i].getAttribute("name")
        var lat = fts[i].getAttribute("lat")
        var lng = fts[i].getAttribute("lng")
        var loc = new google.maps.LatLng(lat,lng);
        //console.log(loc.toUrlValue())
        var infownd = new google.maps.InfoWindow({
          map: map,
          position: loc,
          content: name
          
        });
        infownd.open(map)
    }

}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }

  var options = {
    map: map,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position);
}

google.maps.event.addDomListener(window, 'load', initialize);