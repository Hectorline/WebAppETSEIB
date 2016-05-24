// function genGraph(){
// // document.getElementById("myForm").submit();
// debugger;
// $(document).ready(function(){
// var chart = c3.generate({
    // bindto: '#chart',
    // data: {
      // columns: [
        // ['data1', 30, 200, 100, 400, 150, 250],
        // ['data2', 50, 20, 10, 40, 15, 25]
      // ],
      // axes: {
        // data2: 'y2'
      // },
      // types: {
        // data2: 'bar'
      // }
    // },
    // axis: {
      // y: {
        // label: {
          // text: 'Y Label',
          // position: 'outer-middle'
        // },
        // tick: {
          // format: d3.format("$,") // ADD
        // }
      // },
      // y2: {
        // show: true,
        // label: {
          // text: 'Y2 Label',
          // position: 'outer-middle'
        // }
      // }
    // }
// });
// }
// }
	function changeSection(sec) {
	// debugger;
	var id = document.getElementsByClassName("container");
	var p;
	for(p=0;p<id.length; p++)
		{
		if(p==sec)
			{
				if(!(id[p].classList.contains('active')))
				{
				id[p].classList.add('active');
				}
			}
		else {id[p].classList.remove('active');
				}
		}
	}
