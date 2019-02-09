import { Component, OnInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AgGridNg2 } from 'ag-grid-angular';
import { AuthServiceService, idToken } from '../auth-service.service';

@Component({
  selector: 'app-recommendation',
  templateUrl: './recommendation.component.html',
  styleUrls: ['./recommendation.component.scss']
})
export class RecommendationComponent implements OnInit {
  @ViewChild('agGrid') agGrid: AgGridNg2;

  title = 'MVP Dashboard';
  credentials: idToken = {
    id: ''
  }

  columnDefs = [
    {
      headerName: "url",
      field: "url",
      width: 80
    },
    {
      headerName: "title",
      field: "title",
      width: 230
    }
  ];
  rowData: any;

  constructor(private _authService: AuthServiceService) {
  }

  flipped = false;
  ngOnInit() {
  }
  flipIt() {
    this.flipped = !this.flipped;
  }


  PassId() {
    this._authService.postTwitterID(this.credentials).subscribe((persons) => {

      this.rowData = persons;
    })
  }
}
