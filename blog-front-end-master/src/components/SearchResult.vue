<template>
    <main id="main">

    <!-- ======= Search Results ======= -->
    <section id="search-result" class="search-result">
      <div class="container">
        <div class="row">
          <div class="col-md-9">
       

            <div class="d-md-flex post-entry-2 small-img"  v-for="blog in searchBlog" :key="blog.id">
              <a class="me-4 thumbnail" @click="singleblog(blog.id)">
                <img :src="blog.mainImage" alt="" class="img-fluid">
              </a>
              <div>
                <div class="post-meta"><span class="date">{{blog.category}}</span> <span class="mx-1">&bullet;</span> <span>{{formatDate(blog.date)}}</span></div>
                <h3><a  @click="singleblog(blog.id)">{{blog.title}}</a></h3>
            
                <div class="d-flex align-items-center author">
                 
                  <div class="name">
                    <h3 class="m-0 p-0">{{blog.fname}} {{blog.lname}}</h3>
                  </div>
                </div>
              </div>
            </div>


          </div>
          <div class="col-md-3">
            <div class="aside-block">
              <h3 class="aside-title">Categories</h3>
              <ul class="aside-links list-unstyled">
                <li v-for="category in categories" :key="category.categoryId" @click="searchByCategory(category.categoryId)">{{ category.name}}</li>
              </ul>
            </div>
          </div>

        </div>
        
      </div>
    </section> 

  </main>
</template>

<script>

export default {
  data() {
    return {
      searchBlog: [],
      categories: []
    }
  },
  props: ["categoryId"],
  created(){
    this.fetchDearchBlogs(this.categoryId);
    this.fetchCategories();
  },
  methods:{
    fetchDearchBlogs(categoryId){
     
     console.log(categoryId)

     this.searchBlog = [];  

      fetch('http://127.0.0.1:5000/blogs/category/'+categoryId, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch blogs');
        }
        return response.json();
      })
      .then(data => {

        this.searchBlog = data.map(main => {
        return {
          id: main[0],
          title: main[1],
          mainImage: main[2],
          data:main[3],
          date:main[4],
          category:main[7],
          fname:main[8],
          lname:main[9],
        };
      });
 
      })
      .catch(error => {
      console.error('Error fetching blogs:', error);
      });
    },
     formatDate(dateString) {
      const date = new Date(dateString);
      return new Intl.DateTimeFormat("default", { dateStyle: "long" }).format(
        date
      );
    },
    singleblog(id) {
      this.$router.push({ name: 'blog', params: { id } });
    },
    fetchCategories() {
      fetch('http://127.0.0.1:5000/categories', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch categories');
        }
        return response.json();
      })
      .then(data => {
        this.categories = data.map(category => {
        return {
          categoryId: category[0],
          name: category[1]
        };
      });
      })
      .catch(error => {
      console.error('Error fetching categories:', error);
      });
    },
    searchByCategory(id){
        this.fetchDearchBlogs(id);    
    }
  }
}

</script>
