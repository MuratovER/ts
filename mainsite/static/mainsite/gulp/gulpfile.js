gitconst gulp = require('gulp');
const	sass = require('gulp-sass');
const	sourcemaps = require('gulp-sourcemaps');
const autoprefixer = require('gulp-autoprefixer');
const	watch = require('gulp-watch');

gulp.task('sass-compile', function(){
	return gulp.src('../scss/**/*.sass')
	.pipe(sourcemaps.init())
	.pipe(sass().on('error', sass.logError))
	.pipe(autoprefixer({
		overrideBrowserlist: ["last 10 version"],
		cascade: true
	}))
	.pipe(gulp.dest('../css'))
})

gulp.task('watch', function() {
	gulp.watch('../scss/**/*.sass', gulp.series('sass-compile'))
})