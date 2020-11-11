import { MovieService } from './../movie.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-movielist',
  templateUrl: './movielist.component.html',
  styleUrls: ['./movielist.component.css']
})
export class MovielistComponent implements OnInit {

  movies:any;
  constructor(private movie:MovieService) { }

  ngOnInit(): void {
    this.movie.getMovieList().subscribe((m)=>{
      this.movies = m;
    });
  }

}
