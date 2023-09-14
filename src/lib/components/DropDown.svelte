<script>
	export let options = [];
	let opened = false;
	export let mode = true; //True as in light mode, false for dark
	let color = mode ? 'secondary' : 'primary';
	export let currentOption = 'General inquiry';

	function toggelMenu() {
		opened = !opened;
		document.body.addEventListener('click', handleMenuClose); //Attach a listener on the body to be able to close the menu from outside
	}
	function handleMenuClose() {
		opened = false;
		document.body.removeEventListener('click', handleMenuClose);
	}

	function selectOption(e) {
		currentOption = e.target.innerText;
	}
</script>

<div class="relative inline-block text-left mb-10">
	<label class={`block mb-2 text-sm font-joseph font-meduium text-${color}`}>
		<slot />
	</label>
	<div>
		<button
			on:click|stopPropagation={toggelMenu}
			type="button"
			class={`inline-flex w-full justify-center gap-x-1.5 rounded-md bg-transparent px-3 py-2 text-sm font-semibold text-${color} border-b border-${color} shadow-sm `}
			id="menu-button"
			aria-expanded="true"
			aria-haspopup="true"
		>
			{currentOption}
			<svg
				class={`-mr-1 h-5 w-5 text-${color}`}
				viewBox="0 0 20 20"
				fill="currentColor"
				aria-hidden="true"
			>
				<path
					fill-rule="evenodd"
					d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
					clip-rule="evenodd"
				/>
			</svg>
		</button>
	</div>

	{#if opened}
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<div
			on:click|stopPropagation={() => {}}
			class="absolute left-0 z-10 mt-2 w-56 origin-top-left rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
			role="menu"
			aria-orientation="vertical"
			aria-labelledby="menu-button"
			tabindex="-1"
		>
			<div class="py-1" role="none">
				{#each options as option}
					<!-- svelte-ignore a11y-click-events-have-key-events -->
					<a
						on:click|preventDefault={selectOption}
						class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-200"
						role="menuitem"
						tabindex="-1"
						id="menu-item-0">{option}</a
					>
				{/each}
			</div>
		</div>
	{/if}
</div>
