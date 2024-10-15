var gulp = require('gulp');
var concat = require('gulp-concat');
 
gulp.task('scripts', function(done) {
  return gulp.src('./lib/*.js')
    .pipe(concat('all.js'))
    .pipe(gulp.dest('./dist/'));
    done();
});