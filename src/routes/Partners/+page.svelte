<script>
	/*var copy = document.querySelector("slide-track").cloneNode(true);
	document.querySelector("slide").appendChild(copy);*/
</script>

<div class="slider">
	<div class="slide-track">
		<div class="slide">
			<img src="/GACA.svg" alt="logo" height="100" width="250" />
		</div>
		<div class="slide">
			<img src="/KACST.svg" alt="logo" height="100" width="250" />
		</div>
		<div class="slide">
			<img src="/MCIT.svg" alt="logo" height="100" width="250" />
		</div>
		<div class="slide">
			<img src="/NTDP.svg" alt="logo" height="100" width="250" />
		</div>
		<div class="slide">
			<img src="/SFCPD.svg" alt="logo" height="100" width="250" />
		</div>
		<div class="slide">
			<img src="/GACA.svg" alt="logo" height="100" width="250" />
		</div>
	</div>
</div>

<style>
	.title {
		text-align: center;
	}

 

	@keyframes scroll {
		0% {
			transform: translateX(0);
		}
		90% {
			transform: translateX(calc(-70px *7));
		}
	}

	.slider {
		height: 150px;
		margin: auto;
		overflow: hidden;
		position: relative;
		width: auto;
		background-color: #e9e2d1;
	}

	.slider .slide-track {
		display: inline;
	 
		animation: scroll 30s linear infinite;

		display: flex;
		white-space: nowrap;
		width: calc(250px * 10);
	}
	.slider .slide {
		height: 200px;
		width: 450px;
		margin: 0 20px;

		padding: 40px 0;
	}
</style>
