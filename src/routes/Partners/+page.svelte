<script>
</script>

<section class="partners">
	<div class="slider">
		<h1 class="title">OUR TRUSTED PARTNERS</h1>

		<div class="slide-track">
			<div class="slide">
				<img src="src\lib\assets\images\GACA.svg" alt="logo" height="100" width="250" />
			</div>
			<div class="slide">
				<img src="src\lib\assets\images\KACST.svg" alt="logo" height="100" width="250" />
			</div>
			<div class="slide">
				<img src="src\lib\assets\images\MCIT.svg" alt="logo" height="100" width="250" />
			</div>
			<div class="slide">
				<img src="src\lib\assets\images\NTDP.svg" alt="logo" height="100" width="250" />
			</div>
			<div class="slide">
				<img src="src\lib\assets\images\SFCPD.svg" alt="logo" height="100" width="250" />
			</div>
			<div class="slide">
				<img src="src\lib\assets\images\GACA.svg" alt="logo" height="100" width="250" />
			</div>
		</div>
	</div>
</section>

<style>
	.title {
		margin-top: 40px;
		text-align: center;
		font-size: 28px;
		font-weight: 600;
	}

	@keyframes scroll {
		0% {
			transform: translateX(0);
		}
		90% {
			transform: translateX(calc(-70px * 7));
		}
	}

	.slider {
		height: 235px;
		margin: auto;
		overflow: hidden;
		position: relative;
		width: auto;
		background-color: var(--color-secondary);
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
