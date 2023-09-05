<script>
    export let color= 'primary'
    export let outlined= false
     let attributes = outlined ? `text-${color} border border-1 focus:ring-4 focus:ring-${color}` : `text-white focus:ring-1  bg-${color} hover:bg-${color}-hover focus:ring-${color}-hover`
</script>

<button class={`${attributes} font-light rounded-lg text-md px-5 py-2 mr-2 mb-2 focus:outline-none`}><slot/></button>