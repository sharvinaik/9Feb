import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AuthServiceService } from './auth-service.service';
import { AppComponent } from './app.component';
import { AgGridModule } from 'ag-grid-angular';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import 'ag-grid-enterprise';
import { RecommendationComponent } from './recommendation/recommendation.component';

@NgModule({
  declarations: [AppComponent, RecommendationComponent],
  imports: [BrowserModule, HttpClientModule, AgGridModule.withComponents([]), FormsModule],
  providers: [AuthServiceService],
  bootstrap: [AppComponent]
})
export class AppModule {}