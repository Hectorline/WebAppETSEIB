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
