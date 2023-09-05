<script>
	import Title from './components/title.svelte';
	import Desc from './components/aboutDescription.svelte';
	import Why from './components/whyDunesaeroList.svelte';
</script>

<div class="main-page">
	<div class="about">
		<Title pageTitle="About Us" elementHTML="h1" />
		<Desc />
	</div>
	<div class="why-dunes">
		<Title pageTitle="But, Why Dunes Aero?" elementHTML="p"/>
        <Why />
	</div>
</div>

<style>
	@import './global.css';
	@import '../../app.css';

	.about {
		background-color: var(--color-secondary);
		padding: 75px;
        width: 100%;
	}
	.why-dunes {
		background-color: #FAF4E5;
		padding: 25px;
        width: 100%;
	}

    @media (max-width: 768px) {
		.about {
            padding: 20px;
		}
        .why-dunes {
            padding: 20px;
        }
	}
</style>
