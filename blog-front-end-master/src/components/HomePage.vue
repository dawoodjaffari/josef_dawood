<template>

<main id="main">
    <section id="hero-slider" class="hero-slider">
    <div class="container-md" data-aos="fade-in">
      <div class="row">
        <div class="col-12">
          <div class="container">
          <div class="slider">
            <div v-for="(slide, index) in mainBlog1" :key="index" v-show="currentIndex === index" style=" display: flex;justify-content: center;">
              <a :href="slide.link" class="img-bg d-flex align-items-end" :style="{ backgroundImage: 'url(' + slide.mainImage + ')',width: '1200px' } ">
                <div class="img-bg-inner">
                  <h2>{{ slide.title }}</h2>
                </div>
              </a>
            </div>
          </div>
          </div>
          <div class="custom-swiper-button-next" @click="nextSlide">
            <span class="bi-chevron-right"></span>
          </div>
          <div class="custom-swiper-button-prev" @click="prevSlide">
            <span class="bi-chevron-left"></span>
          </div>
        </div>
      </div>
    </div>
    </section>

    <!-- ======= Post Grid Section ======= -->
    <section id="posts" class="posts">
      <div class="container" data-aos="fade-up">
        <div class="row g-5">
          <div class="col-lg-4">
            <div class="post-entry-1 lg" v-for="main in mainBlog" :key="main.id">
              <a @click="singleBlog(main.id)"><img :src="main.mainImage" alt="" class="img-fluid"></a>
              <div class="post-meta"><span class="date">{{main.category}}</span> <span class="mx-1">&bullet;</span> <span>{{formatDate(main.date)}}</span></div>
              <h2><a @click="singleBlog(main.id)">{{main.title}}</a></h2>
              <div class="d-flex align-items-center author">
                
                <div class="name">
                  <h3 class="m-0 p-0">{{main.fname}} {{main.lname}}</h3>
                </div>
              </div>
            </div>

          </div>

          <div class="col-lg-8">
            <div class="row g-5">
              <div class="col-lg-4 border-start custom-border">
                <div class="post-entry-1" v-for="main in mainBlog1" :key="main.id">
                  <a  @click="singleBlog(main.id)"><img :src="main.mainImage" alt="" class="img-fluid"></a>
                  <div class="post-meta"><span class="date">{{main.category}}</span> <span class="mx-1">&bullet;</span> <span>{{formatDate(main.date)}}</span></div>
                  <h2><a @click="singleBlog(main.id)" >{{main.title}}</a></h2>
                </div>
              </div>
              <div class="col-lg-4 border-start custom-border">
                <div class="post-entry-1" v-for="main in mainBlog2" :key="main.id">
                  <a  @click="singleBlog(main.id)"><img :src="main.mainImage" alt="" class="img-fluid"></a>
                  <div class="post-meta"><span class="date">{{main.category}}</span> <span class="mx-1">&bullet;</span> <span>{{formatDate(main.date)}}</span></div>
                  <h2><a @click="singleBlog(main.id)">{{main.title}}</a></h2>
                </div>
                
              </div>
              <div class="col-lg-4 border-start custom-border">
                <div class="post-entry-1" v-for="main in mainBlog3" :key="main.id">
                  <a  @click="singleBlog(main.id)"><img :src="main.mainImage" alt="" class="img-fluid"></a>
                  <div class="post-meta"><span class="date">{{main.category}}</span> <span class="mx-1">&bullet;</span> <span>{{formatDate(main.date)}}</span></div>
                  <h2><a @click="singleBlog(main.id)">{{main.title}}</a></h2>
                </div>
              </div>

            
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
      currentIndex: 0,
      mainBlog: [],
      mainBlog1:[],
      mainBlog2:[],
      mainBlog3:[],
      categories:[],
      dividedArrays: [],
      dividedArrays1: [],
      dividedArrays2: [], 
      slideInterval: null, 
      intervalDuration: 4000,
    };
  },
  mounted(){
     this.startSlideInterval();
  },
  created() {
    this.fetchMainBlogs();
    this.fetchMainBlogs1();
    this.fetchMainBlogs2();
    this.fetchMainBlogs3();
    this.fetchCategories();
  },
  methods: {
    startSlideInterval() {
      this.slideInterval = setInterval(() => {
        this.nextSlide(); 
      }, this.intervalDuration);
    },
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % 3;
    },
    prevSlide() {
      this.currentIndex = (this.currentIndex - 1 + 3) %3;
    },
    singleBlog(id){
      this.$router.push({ name: 'blog', params: { id } });
    },
    fetchMainBlogs(){
      fetch('http://127.0.0.1:5000/blogs/page/1/1', {
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
        console.log(data)
        this.mainBlog = data.map(main => {
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
      console.log("work")
      console.log(this.mainBlog)
      })
      .catch(error => {
      console.error('Error fetching categories:', error);
      });
    },
    fetchMainBlogs1(){
      fetch('http://127.0.0.1:5000/blogs/page/1/3', {
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
        console.log(data)
        this.mainBlog1 = data.map(main => {
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
      console.error('Error fetching categories:', error);
      });
    },
    fetchMainBlogs2(){
      fetch('http://127.0.0.1:5000/blogs/page/2/3', {
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
        console.log(data)
        this.mainBlog2 = data.map(main => {
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
      console.error('Error fetching categories:', error);
      });
    },
    fetchMainBlogs3(){
      fetch('http://127.0.0.1:5000/blogs/page/3/3', {
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
        this.mainBlog3 = data.map(main => {
        return {
          id: main[0],
          title: main[1],
          mainImage: main[2],
          data:main[3],
          date:main[4],
          category:main[7],
          fname:main[8],
          lname:main[9],
          dividedArrays: [],
          dividedArrays1: [],
          dividedArrays2: []
        };
      });
 
      })
      .catch(error => {
      console.error('Error fetching categories:', error);
      });
    },
    formatDate(dateString) {
            const date = new Date(dateString);
            return new Intl.DateTimeFormat('default', {dateStyle: 'long'}).format(date);
    },
    getAllCategoryDataTop(id){
      
      fetch('http://127.0.0.1:5000/blogs/category/'+id+'/1/9', {
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
        this.cateTopBlogs = data.map(main => ({
          id: main[0],
          title: main[1],
          mainImage: main[2],
          data:main[3],
          date:main[4],
          category:main[7],
          fname:main[8],
          lname:main[9],
      }));
      
  
      })
      .catch(error => {
      console.error('Error fetching categories:', error);
      });
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
        this.categories = data.map(category => ({
          categoryId: category[0],
          name: category[1]        
        }));
   
      })
      .catch(error => {
      console.error('Error fetching categories:', error);
      });
      
   },

  }
}
</script>

<style scoped>
.slider {
  overflow: hidden;
  position: relative;
  width: 100%;
}

.slide {
  display: none;
}

.show-slide {
  display: block;
}

.custom-swiper-button-next,
.custom-swiper-button-prev {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
}

.custom-swiper-button-next {
  right: 10px;
}

.custom-swiper-button-prev {
  left: 10px;
}
</style>