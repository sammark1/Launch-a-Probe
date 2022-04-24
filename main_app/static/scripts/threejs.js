import * as THREE from 'three';
import render_data from './render_data.json' assert {type:'json'}


const displayZone = [innerWidth,innerHeight];

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75,displayZone[0]/displayZone[1], 0.1, 1000);
const renderer = new THREE.WebGLRenderer({antialias:true});

renderer.setSize(displayZone[0],displayZone[1]);
renderer.setPixelRatio(devicePixelRatio);
document.body.appendChild(renderer.domElement);

const light1 = new THREE.PointLight( 0xffa000, .6, 100 )
const light2 = new THREE.PointLight( 0xffa0a0, .7, 100 )
const light3 = new THREE.PointLight( 0x2000ff, .5, 100 )
const testAmbLight = new THREE.AmbientLight( 0x500070, .25 )

const texture = new THREE.TextureLoader().load('/static/images/fractal-noise.jpg')
const icosphere = new THREE.IcosahedronGeometry(1,12);
const icoMaterial = new THREE.MeshPhongMaterial({
    color: render_data.bodyColor,
    bumpMap: texture,
    // displacementMap: texture,
});
//const icoMaterial = new THREE.LineBasicMaterial();
const icoplanet = new THREE.Mesh(icosphere,icoMaterial);

light1.position.set(0,12,0);
light2.position.set(12,8,10);
light3.position.set(-6,-12,0);

scene.add(icoplanet);
scene.add(light1);
scene.add(light2);
scene.add(light3);
scene.add(testAmbLight)

light1.target = icoplanet;

camera.position.z = 5;


function animate () {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    // icoplanet.rotation.x +=0.007;
    icoplanet.rotation.y +=0.01;
    // icoplanet.position.x+=0.02;
    // if (icoplanet.position.x>=8){
    //     icoplanet.position.x=-8;
    // }
}


animate()

console.log()