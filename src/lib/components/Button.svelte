<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    export let color= 'primary'
    export let outlined= false
    export let type='button'
     let attributes = outlined ? `text-${color} border border-1 focus:ring-4 focus:ring-${color}` :
      `text-${color==='primary' | color==='tertiary'?'white':'primary'} focus:ring-1  bg-${color} hover:bg-${color}-hover focus:ring-${color}-hover`
</script>

<button
on:click={()=>{  dispatch("navigate");}}
type={type}
class={`${attributes}  rounded-lg font-medium text-md px-5 py-2 mr-2 mb-2 focus:outline-none`}><slot/></button>