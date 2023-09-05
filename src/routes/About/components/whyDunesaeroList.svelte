<!-- Problem: Fix the item position (div -> item), The logo goes to the top when there are two lines on the text -->

<script>
	import Local from '$lib/assets/images/local icon.svg';
	import Advanced from '$lib/assets/images/advanced icon.svg';
	import Maintenance from '$lib/assets/images/maintenance icon.svg';
	import Train from '$lib/assets/images/train icon.svg';
	import Customize from '$lib/assets/images/customize icon.svg';
	import Package from '$lib/assets/images/package icon.svg';
	import Regularity from '$lib/assets/images/regularity icon.svg';
	import Experts from '$lib/assets/images/experts icon.svg';
</script>

<div class="container">
	<div class="list-items">
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Local} alt="Error" />
			</div>
			<p class="item-text">Locally developed system</p>
		</div>
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Advanced} alt="Error" />
			</div>
			<p class="item-text">Advanced AI detection software</p>
		</div>
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Maintenance} alt="Error" />
			</div>
			<p class="item-text">Extensive support & maintenance</p>
		</div>
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Train} alt="Error" />
			</div>
			<p class="item-text">Training Programs</p>
		</div>
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Customize} alt="Error" />
			</div>
			<p class="item-text">Customiazale drone systems</p>
		</div>
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Package} alt="Error" />
			</div>
			<p class="item-text">Full system package</p>
		</div>
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Regularity} alt="Error" />
			</div>
			<p class="item-text">Regulatory Compliance</p>
		</div>
		<div class="item">
			<div class="img-back">
				<img class="item-logo" src={Experts} alt="Error" />
			</div>
			<p class="item-text">Experts in drone systems</p>
		</div>
	</div>
</div>

<style>
	@import '../global.css';

	.list-items {
		display: grid;
		grid-template-columns: repeat(4, 1fr); /* 4 equal-width columns */
		gap: 50px; /* Adjust the gap between items as needed */
		padding: 45px 0;
	}
	.item {
		display: flex;
		flex-direction: column;
		width: 100%;
		justify-content: center;
		align-items: center;
	}
	.item-logo {
		max-width: 100%;
		width: 105px;
		height: 105px;
		padding: 5px;
		justify-content: center;
		overflow: hidden;
	}

	.img-back {
		background: var(--color-primary);
		border-radius: 50%;
		width: 140px; /* Adjust the width as needed */
		height: 140px; /* Adjust the height as needed */
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.item-text {
		margin-top: 10px;
		text-align: center;
		font-size: 17px;
	}
	/* Responsive styles */
	@media screen and (max-width: 768px) {
		.list-items {
			grid-template-columns: repeat(2, 1fr); /* 2 columns on small screens */
			gap: 30px;
			padding: 35px 0;
		}
		.item-logo {
			width: 75px;
			height: 75px;
			padding: 3px;
		}

		.img-back {
			width: 100px; /* Adjust the width for small screens */
			height: 100px; /* Adjust the height for small screens */
		}
		.item-text {
			font-size: 13px;
		}
	}
</style>
